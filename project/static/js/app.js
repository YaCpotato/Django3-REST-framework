window.onload = function () {
  var fileArea = document.getElementById('uploadForm');
  var fileInput = document.getElementById('csvArea');
  fileArea.addEventListener('drop', function(evt){
    evt.preventDefault();
    fileArea.classList.remove('dragenter');
    var files = evt.dataTransfer.files;
    fileInput.files = files;
  });
};

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

function uploadFile(e) {
  var files = e.target.files;

  var csrftoken = getCookie('csrftoken');

  for (var i = 0; i < files.length; i++) {
      var XHR = new XMLHttpRequest();
      XHR.open('POST', '/csv');
      var data = new FormData();
      XHR.setRequestHeader("X-CSRFToken", csrftoken);
      data.append('csv', files[i], files[i].name); // ファイル情報を送信データとして設定
      XHR.send(data)
  }
  $('.toast').toast('show',delay=1000)
}