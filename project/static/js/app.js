function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

var fileArea = document.getElementById('csvArea');


fileArea.addEventListener('dragover', function(event){
  event.preventDefault();
  fileArea.classList.add('dragover');
});

fileArea.addEventListener('dragleave', function(event){
    event.preventDefault();
    fileArea.classList.remove('dragover');
});
fileArea.addEventListener('drop', function(event){
    event.preventDefault();
    fileArea.classList.remove('dragenter');
    var files = evt.dataTransfer.files;
    fileArea.files = files;
});

function uploadFile(e) {
  var files = e.target.files;

  var csrftoken = getCookie('csrftoken');

  for (var i = 0; i < files.length; i++) {
      var XHR = new XMLHttpRequest();
      XHR.open('POST', '/csv');
      var data = new FormData();
      XHR.setRequestHeader("X-CSRFToken", csrftoken);
      data.append(files[i].name, files[i]); // ファイル情報を送信データとして設定
      XHR.send(data)
  }
  $('.toast').toast('show',delay=1000)
}