
              $(function(){
                
                $("#usLogin").click(function(){
                  var usemial = $("#usEmail").val()
                  var uspassword = $("#usPassword").val()
                  var userInfo = {
                  'email':usemial,
                  'password':uspassword
                }
                  $.ajax({
                    url:'http://176.215.122.8:8000/v1/ustoken',
                    type:'POST',
                    contentType:"application/json",
                    dataType:'json',
                    data:JSON.stringify(userInfo),
                    success:function(res){
                      if (res.code == 200){
                        alert("登陆成功")
                        window.localStorage.setItem('cofst_token',res.data.token);
                        window.localStorage.setItem('cofst_userid',res.data.userId);
                        window.location.href = '/index';
                      }else{
                        alert(res.error)
                      }

                    },
                  })
                })

              })