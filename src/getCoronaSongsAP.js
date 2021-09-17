// https://apnews.com/article/entertainment-music-luke-combs-pandemics-hip-hop-and-rap-2a49e686206f00c6f74d5d132225bc4a

// creates two arrays that either include corona artists or corona songs
coronaArtists = []
coronaSongs = []
entries = document.querySelectorAll('p.Component-root-0-2-61')
for(let i=0; i<entries.length; i++){
    text = entries[i].childNodes[0].textContent
    n = +text.replace('. ', '')
    if(!isNaN(n)) {
        coronaArtists.push(entries[i].childNodes[1].text.split(', “')[0].replace('“', ''))
        coronaSongs.push(entries[i].childNodes[1].text.split(', “')[1].replace('“', ''))
    }
}


