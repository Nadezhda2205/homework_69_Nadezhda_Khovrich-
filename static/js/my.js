let buttonAdd = document.getElementById('add');
let buttonSubtract = document.getElementById('subtract');
let buttonMultiply = document.getElementById('multiply');
let buttonDivide = document.getElementById('divide');

buttonAdd.addEventListener('click', function(e){
    e.preventDefault();
    sendRequest('add');
})
buttonSubtract.addEventListener('click', function(e){
    e.preventDefault();
    sendRequest('subtract');
})
buttonMultiply.addEventListener('click', function(e){
    e.preventDefault();
    sendRequest('multiply');
})
buttonDivide.addEventListener('click', function(e){
    e.preventDefault();
    sendRequest('divide')
})

function sendRequest(action){
    url = `http://127.0.0.1:8000/${action}/`
    return fetch(url, {
        method: 'POST',
        body: JSON.stringify(
            {
                "A": Number(document.getElementById('id_numder_a').value),
                "B": Number(document.getElementById('id_numder_b').value)
            }),
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        const container = document.getElementById('container')
        const div = document.createElement('div')
        if (data.answer !== undefined){
            container.appendChild(div).innerHTML = `<span style="color: green">${data.answer}</span>`;
        }
        else{
            container.appendChild(div).innerHTML = `<span style="color: red">${data.error}</span>`;
        }
    })
}
