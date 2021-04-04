 var request = new XMLHttpRequest()

 function absolute(relative) {

    base = 'http://127.0.0.1:5000/';
    var stack = base.split("/");
    var parts = relative.split("/");
    // console.log(parts)
    // console.log(stack)
    stack.pop();
    for (var i=0; i<parts.length; i++) {
        stack.push(parts[i]);
    }
    absolute_path = stack.join("/");
    return absolute_path;
}

        // console.log(document.getElementById('playId').src)

 document.getElementById("play_resume_pause_btn").onclick=function(){
    if(document.getElementById('playId').src === absolute('static/images/play.png')){
        document.getElementById('playId').src = absolute('static/images/pause.png');
        request.open('GET' ,'http://127.0.0.1:5000/resume', true)
        request.send()
    } else {
        if (document.getElementById('playId').src === absolute('static/images/pause.png')) {
            document.getElementById("playId").src = absolute('static/images/play.png');
            request.open('GET', 'http://127.0.0.1:5000/pause', true)
            request.send()
        }
    }
};


document.getElementById("next_btn").onclick=function(){
    document.getElementById('playId').src = absolute('static/images/pause.png');
    request.open('GET', 'http://127.0.0.1:5000/next', true)
    request.send()
};

document.getElementById("pre_btn").onclick=function(){
    document.getElementById('playId').src = absolute('static/images/pause.png');
    request.open('GET', 'http://127.0.0.1:5000/previous', true)
    request.send()
};