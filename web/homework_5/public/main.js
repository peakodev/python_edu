console.log('Hello world!')

const ws = new WebSocket('ws://localhost:8080')

let formChat = document.getElementById('formChat')
let textField = document.getElementById('textField')
let subscribe = document.getElementById('subscribe')

formChat.addEventListener('submit', function (e) {
    e.preventDefault()
    ws.send(textField.value)
    textField.value = null
})

ws.addEventListener('open', function (e) {
    console.log('Hello WebSocket!')
})

ws.addEventListener('message', function (e) {
    try {
        console.log(e.data)
        const elMsg = document.createElement('div')
        elMsg.textContent = e.data
        subscribe.appendChild(elMsg)
    } catch (e) {
        console.log('Error:', e)
    }
})
