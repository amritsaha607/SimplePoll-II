function register() {
  var sendData = {
    "csrfmiddlewaretoken": csrf_token,
    "mode": "register",
    "username": $("#signUpModal #id_username").val(),
    "password": $("#signUpModal #id_password").val(),
  };
  $.ajax({
    url: authenticationURL,
    type: 'POST',
    data: sendData,
    success: function (data) {
      if (data.response == "ok") { window.location.reload(); }
      else { alert(data.response); }
    },
    error: () => { alert("Something went wrong"); },
    cache: false,
  });
}

function login() {
  var sendData = {
    "csrfmiddlewaretoken": csrf_token,
    "mode": "login",
    "username": $("#loginModal #id_username").val(),
    "password": $("#loginModal #id_password").val(),
  };
  $.ajax({
    url: authenticationURL,
    type: 'POST',
    data: sendData,
    success: function (data) {
      if (data.response == "ok") { window.location.reload(); }
      else { alert(data.response); }
    },
    error: () => { alert("Something went wrong"); },
    cache: false,
  });
}

function logout() {
  var sendData = {
    "csrfmiddlewaretoken": csrf_token,
    "mode": "logout",
  };
  $.ajax({
    url: authenticationURL,
    type: 'POST',
    data: sendData,
    success: function (data) {
      if (data.response == "ok") { window.location.reload(); }
      else { alert(data.response); }
    },
    error: () => { alert("Something went wrong"); },
    cache: false,
  });
}

$("#btn_register").on('click', register);
$("#btn_login").on('click', login);
$("#btn_logout").on('click', logout);
