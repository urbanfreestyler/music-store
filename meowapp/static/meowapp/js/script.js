const musicContainer = document.querySelector('.music-container')
const playBtn = document.querySelector('#play')
const prevBtn = document.querySelector('#prev')
const nextBtn = document.querySelector('#next')
const audio = document.querySelector('#audio')
const bpm = document.querySelector('#bpm')
const key = document.querySelector('#key')
const progress = document.querySelector('.progress')
const progressContainer = document.querySelector('.progress-container')
const title = document.querySelector('#title')
const cover = document.querySelector('#cover')

let songIndex = 0


fetch('http://127.0.0.1:8000/beats/')
    .then(response => {
        return response.json()
    })
    .then(data => {
        // Work with JSON data here
        let songs = data


        loadSong(songs[songIndex])

        function loadSong(song) {
            title.innerText = song.title;
            audio.src = song.audio;
            cover.src = song.cover;
        }

        // Update song details

        function playSong() {
            musicContainer.classList.add('play')
            playBtn.querySelector('i.fas').classList.remove('fa-play')
            playBtn.querySelector('i.fas').classList.add('fa-pause')

            audio.play()
        }

        function pauseSong() {
            musicContainer.classList.remove('play')
            playBtn.querySelector('i.fas').classList.remove('fa-pause')
            playBtn.querySelector('i.fas').classList.add('fa-play')

            audio.pause()
        }

        function prevSong() {
            songIndex--

            if(songIndex < 0) {
                songIndex = songs.length - 1
            }

            loadSong(songs[songIndex])

            playSong()
        }

        function nextSong() {
            songIndex++

            if(songIndex > songs.length - 1) {
                songIndex = 0
            }

            loadSong(songs[songIndex])

            playSong()
        }


        function updateProgress(e) {
            const {duration, currentTime} = e.srcElement
            const progressPercent = (currentTime / duration) * 100

            progress.style.width = `${progressPercent}%`

        }

        function setProgress(e) {
            const width = this.clientWidth
            const clickX = e.offsetX
            const duration = audio.duration

            audio.currentTime = (clickX / width) * duration
        }

        playBtn.addEventListener('click', () => {
            const isPlaying = musicContainer.classList.contains('play')

            if(isPlaying) {
                pauseSong()
            }
            else{
                playSong()
            }
        })



        // Change song events

        prevBtn.addEventListener('click', prevSong)
        nextBtn.addEventListener('click', nextSong)

        audio.addEventListener('timeupdate', updateProgress)

        progressContainer.addEventListener('click', setProgress)

        audio.addEventListener('ended', nextSong)

    })
    .catch(err => {
        // Do something for an error here
    })


