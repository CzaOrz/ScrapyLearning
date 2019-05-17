import logging
import pymongo

from czaSpider.dataBase.config import MONGO_INFO
from czaSpider.czaTools import merge_dict


def get_mongo_client():
    global client
    try:
        client = pymongo.MongoClient(**MONGO_INFO)
    except:
        logging.warning('create Mongodb Client Error!')
        return 0
    else:
        logging.info('Mongodb Client Create Success!')
        return 1


def process_commands(all=None, size=None, ne=None, gt=None, gte=None, lt=None, lte=None, **kwargs):
    commands = []
    if kwargs:
        commands.append(kwargs)
    if all:  # {key:[v1,v2]}
        commands.append({key: {"$all": value} for key, value in all.items()})
    if size:  # {key:value}
        commands.append({key: {"$size": value} for key, value in size.items()})
    if ne:
        commands.append({key: {"$ne": value} for key, value in ne.items()})
    if gt:
        commands.append({key: {"$gt": value} for key, value in gt.items()})
    if gte:
        commands.append({key: {"$gte": value} for key, value in gte.items()})
    if lt:
        commands.append({key: {"$lt": value} for key, value in lt.items()})
    if lte:
        commands.append({key: {"$lte": value} for key, value in lte.items()})
    return commands


class BaseMongodb(object):
    def __init__(self, dbName, collName):
        self.dbName = dbName
        self.collName = collName
        global client
        self.client = client
        self.database = self.client[dbName]
        self.collection = self.database[collName]
        self._docs = self.collection.count()
        self._documents = None

    @property
    def documents(self):
        res = self._documents
        self._documents = None
        return res

    @property
    def docs(self):
        res = self._docs
        self._docs = None
        return res

    def find(self, all=None, size=None, ne=None, gt=None, gte=None, lt=None, lte=None, **kwargs):
        commands = process_commands(all, size, ne, gt, gte, lt, lte, **kwargs)
        query = {"$and": commands} if commands else {}
        self._documents = self.collection.find_one(query)
        return self

    def findAll(self, all=None, size=None, ne=None, gt=None, gte=None, lt=None, lte=None, field=None, **kwargs):
        commands = process_commands(all, size, ne, gt, gte, lt, lte, **kwargs)
        query = {"$and": commands} if commands else {}
        self._documents = [doc[[i for i in field.keys()][0]] if field and len(field) == 1 else doc for doc in
                           self.collection.find(query, field)]
        if field and len(field) != 1:
            self._documents = [[d for d in doc.values()] for doc in self._documents]
        return self

    def pop(self, all=None, size=None, ne=None, gt=None, gte=None, lt=None, lte=None, **kwargs):
        commands = process_commands(all, size, ne, gt, gte, lt, lte, **kwargs)
        query = {"$and": commands} if commands else {}
        self._documents = self.collection.find_one_and_delete(query)
        return self

    def update(self, set=None, unset=None, upsert=False, **kwargs):  # update one document,
        command = dict()
        if set:
            command = {"$set": set}
        elif unset:
            command = {"$unset": set}
        self.collection.update_one(kwargs, command, upsert=upsert)
        self._docs = self.collection.count()
        return self

    def updateAll(self, set=None, unset=None, upsert=False, **kwargs):
        command = dict()
        if set:
            command = {"$set": set}
        elif unset:
            command = {"$unset": set}
        self.collection.update_many(kwargs, command, upsert=upsert)
        self._docs = self.collection.count()
        return self

    def insert(self, new_document=None, **kwargs):  # insert_one(dict)3
        self.collection.insert_one(new_document or kwargs)
        self._docs = self.collection.count()
        return self

    def insertAll(self, new_documents_list):  # insert_many(list)
        self.collection.insert_many(new_documents_list)
        self._docs = self.collection.count()
        return self

    def remove(self, **kwargs):
        self.collection.delete_one(kwargs)
        self._docs = self.collection.count()
        return self

    def removeAll(self, **kwargs):
        self.collection.delete_many(kwargs)
        self._docs = self.collection.count()
        return self

    def drop(self, name=None):
        name = name if name else self.collName
        self.database.drop_collection(name)
        return self


class SourceDB(BaseMongodb):
    def __init__(self, dbName, collName):
        super(SourceDB, self).__init__(dbName + "-source", collName)


class ResolverDB(BaseMongodb):
    def __init__(self, dbName, collName):
        super(ResolverDB, self).__init__(dbName + "-parsing", collName)
