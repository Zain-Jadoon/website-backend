console.log("hello world ")
function postsomething(){
    console.log("this is a post test")
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://172.27.121.253:5002/transact", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
    "from": "Zain",
    "from_passwd": "hello",
    "to": "Zaid",
    "ammount": "100"
    }));
    console.log(xhr.responseText);
}