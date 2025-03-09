  // Web Speech API integration
  var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  
  document.getElementById('recordBtn').onclick = function() {
    recognition.start();
  };
  
  recognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript;
    document.getElementById('transcript').value = transcript;
    alert('You said: ' + transcript);
  };
  
  document.getElementById('readingForm').onsubmit = async function(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/process_reading', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    document.getElementById('result').innerText = 'Accuracy: ' + data.accuracy;
  };
