__goal__ = "js"
"""
通过内置的data-API可以使用所有的js插件
【模态框】
能够动态谈下来的那种框框，使用的class="modal fade" role="dialog" data-dismiss="modal" aria-label="Close"
首先是一个大类<div class="modal-dialog" role="document">用来包括所有的内容
然后用一个<div class="modal-content">来包括所有的内容
里面的细节就是class="modal-header" / "modal-body" / "modal-footer"

这个务必添加role和aria-labelledby属性，且需要在标题中的按钮中添加aria-hidden="true"属性
这里的fade是用来控制淡入淡出的，很好看啊
class="modal fade" role="dialog"
    class="modal-dialog" role="document"
        class="modal-content"
            class="modal-header"
            class="modal-nody"
            class="modal-footer"
如果要添加栅格栏，或者表单，我们可以在body里面进行定义

【dropdown】
$('#myDropdown').on('show.bs.dropdown', function(){
    //do something
})

实现动态切换，可以使用
$('#myTabs a').click(function(e){
    e.preventDefault()
    $(this).tab('show')
})
$('#myTabs a[href="#profile"]').tab('show')
$('#myTabs a:first').tab('show')

可以对按钮添加动态信息
<button type="button" class="btn" data-toggle="tooltip" data-placement="left" title="Hello World">


nav nav-sidebar

"""



"""echarts note
title: { // 图的标题
    text: '补给站'
},

legend: { // 图的说明栏，可以定义在左边或右边
    orient: 'vertical',
    x: 'left',
    data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
},


"""


