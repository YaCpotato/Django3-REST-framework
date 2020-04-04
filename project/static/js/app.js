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
  for (var i = 0; i < files.length; i++) {
      var xmlHttpRequest = new XMLHttpRequest();
      xmlHttpRequest.open('POST', 'api/csv');
      xmlHttpRequest.setRequestHeader('Content-Type', 'multipart/form-data; charset=utf-8');
      var data = new FormData();
      data.append(files[i].name, files[i]); // ファイル情報を送信データとして設定
      xmlHttpRequest.send(data);
  }
  $('.toast').toast('show',delay=1000)
}