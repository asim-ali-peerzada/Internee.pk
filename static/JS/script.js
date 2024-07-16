const words = ['Get a Compatative Job?', 'On Your Desire Domain?', 'Get Hands On Experience']; // Update with your desired text
let wordIndex = 0;
let letterIndex = 0;
let direction = 1; // 1 for typing, -1 for deleting

function typeWriter() {
  const currentWord = words[wordIndex];
  const displayedText = currentWord.slice(0, letterIndex);

  document.querySelector('.typewriter h2').textContent = displayedText;

  if (direction === 1) {
    // Typing
    letterIndex++;
    if (letterIndex <= currentWord.length) {
      setTimeout(typeWriter, 100); // Typing speed
    } else {
      direction = -1;
      setTimeout(typeWriter, 1000); // Pause after typing
    }
  } else {
    // Deleting
    letterIndex--;
    if (letterIndex >= 0) {
      setTimeout(typeWriter, 50); // Deleting speed
    } else {
      direction = 1;
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(typeWriter, 500); // Pause before typing next word
    }
  }
}

typeWriter();
