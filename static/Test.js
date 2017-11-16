(function(){
var form = document.forms["score"];
EventUtil.addHandler(form,"submit",function(event){
    event=EventUtil.getEvent(event);
    var target=EventUtil.getTarget(event);
    var id= target.elements["id"];
    var cet4=target.elements["cet4"];
    var bioChem=target.elements["bioChem"];
    if (! /[\d]{10}/.test(id.value)){
    id.focus();
    return }

    if (! /[\d\.]{3,5}/.test(cet4.value)){
    cet4.focus();
    return }
    if (! /[\d\.]{1,3}/.test(bioChem.value)){
    cet4.focus();
    return }
    target.submit();
})
})()