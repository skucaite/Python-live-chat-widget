$(document).ready(function() {

// Global variables
  var message_socket = io('http://127.0.0.1:5000/message');

// Open and close user chatbox window
  $('#open-button').on('click', function() {
    document.getElementById("my_form").style.display = "block";
  });

  $('.close').on('click', function() {
    document.getElementById("my_form").style.display = "none";
    document.getElementById("chat_form").style.display = "none";
  });

// Open one of chat in admin dashboard
  $('.-open_chat').on('click', function() {
    // document.getElementById("chat_window").style.display = "block";        // Display different view before opening any chat?
    const $el = $(this)
    const username = $el.data('user')
    const room = $el.data('room')
    document.getElementById('room_name').innerText = 'CHAT WHIT: ' + username;
    document.getElementById('admin_chatbox').innerText = 'Loading..';
    document.getElementById('room').innerText = room;
    message_socket.emit('chat_menu', {'username' : username, 'room' : room });
  });


// Load incoming past messages
  message_socket.on('show_past_messages', function(past_messages) {
    document.getElementById('admin_chatbox').innerHTML = past_messages;
  });

// Get username and create room
  $('#name_button').on('click', function() {
    message_socket.emit('username', $('#username').val());
    document.getElementById("chat_form").style.display = "block";
    document.getElementById("my_form").style.display = "none";
  });

  message_socket.on('creat_room', function(room) {
    document.getElementById('user_room').innerText = room;
  });

// Send user messages
  $('#user_send').on('click', function() {
    var sender = document.getElementById('username').value;
    var message_to_send = document.getElementById('my_message').value;
    var room = document.getElementById('user_room').innerText;
    document.getElementById('my_message').value = '';
    message_socket.emit('user_message', {'username' : sender, 'message' : message_to_send, 'room' : room });
  });

// Send admin messages
  $('#admin_send').on('click', function() {
    var message_to_send = $('#admin_message').val();
    var room = document.getElementById('room').innerText;
    document.getElementById('admin_message').value = '';
    message_socket.emit('admin_message', {'room' : room, 'message' : message_to_send});
  });

// Message append to chatboxes
  message_socket.on('print_message', function(msg) {
    $('#user_chatbox').append(msg+'<br>');
    $('#admin_chatbox').append(msg+'<br>');
  });

// GET INPUTS BY PRESSING ENTER
  $("#username").keyup(function(event) {
      if (event.keyCode === 13) {
          $("#name_button").click();
      }
  });

  $("#my_message").keyup(function(event) {
      if (event.keyCode === 13) {
          $("#user_send").click();
      }
  });

  $("#admin_message").keyup(function(event) {
      if (event.keyCode === 13) {
          $("#admin_send").click();
      }
  });

});
