document.addEventListener('DOMContentLoaded', (event) => {

    let btnCopyUrl = document.querySelector('#btnCopyUrl');

    btnCopyUrl.addEventListener('click', (event) => {
        event.preventDefault; 
        
        // if you want to copty the URL from the browser
        //  let url = window.location.href;

        let sUrl = document.querySelector('#shortUrl').innerHTML;
        let fullUrl = `http://localhost:8000/${sUrl}`;

        document.querySelector('#fullUrl').innerHTML = fullUrl;
        
        let url_text = document.querySelector('#fullUrl').innerHTML;
        console.log('Copied text: ', url_text);
        var dummy_input_element = document.createElement('input');

        document.body.appendChild(dummy_input_element);
        dummy_input_element.value = url_text;
        dummy_input_element.select();
        document.execCommand('copy');
        document.body.removeChild(dummy_input_element);
        btnCopyUrl.innerHTML = "URL Copied..."
        btnCopyUrl.classList.add('disabled');
    });
    
})


