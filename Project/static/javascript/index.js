function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#blah')
        .attr('src', e.target.result)
        .width(auto)
        .height(630);
    };

    reader.readAsDataURL(input.files[0]);
  }
}
  $(function() {
      $("form#add_pro_form").submit (function () {
        var formData = new FormData(this);
        axios.post('http://127.0.0.1:8000/handleUpload', formData, {headers: {
    'Access-Control-Allow-Credentials' : true,
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Methods':'GET',
    'Access-Control-Allow-Headers':'application/json',
  }})
        .then((resp) => {
          //document.getElementById('img_here').innerHTML = "<img alt='img' src='" + resp.data + "'/>";        
 document.getElementById('demo_pic').innerHTML = "<iframe src='http://127.0.0.1:8000/img_show/" + resp.data + "'></iframe>";
//window.open('http://127.0.0.1:8000/img_show/' + resp.data,'_blank');  
	console.log(resp.data)
        })
      });
    });

