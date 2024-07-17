How It Works

  Initialize Pygame Mixer: The script initializes the Pygame mixer module to handle audio playback.

  Load Alarm Sound: The alarm sound (in MP3 format) is loaded into the mixer.

  Clear Terminal: Two ANSI escape codes are defined to clear the terminal screen and return the cursor to the home position.

  Countdown Timer: The Alarm function takes a number of seconds as input and starts a countdown timer. During the countdown, the terminal is updated every second to display the remaining time.

  Play Alarm: When the countdown reaches zero, the alarm sound is played. The script waits until the alarm sound finishes playing before terminating.
