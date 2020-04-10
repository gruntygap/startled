console.log('setting up...');

let red, green, blue, lum, redLab,
    greenLab, blueLab, lumLab, output;
const base = new URL('http://192.168.1.69:8080');

window.onload = function() {
    console.log('window loaded!');
    // Global Variables
    // slider vars
    red = document.getElementById('redVal');
    green = document.getElementById('greenVal');
    blue = document.getElementById('blueVal');
    lum = document.getElementById('lumVal');
    // label vars
    redLab = document.getElementById('redLab');
    greenLab = document.getElementById('greenLab');
    blueLab = document.getElementById('blueLab');
    lumLab = document.getElementById('lumLab');
    output = document.getElementById('output');
    // Sliders
    red.onchange = specialColor;
    green.onchange = specialColor;
    blue.onchange = specialColor;
    lum.onchange = specialColor;
    // Setting labels
    redLab.innerHTML = red.value;
    greenLab.innerHTML = green.value;
    blueLab.innerHTML = blue.value;
    lumLab.innerHTML = lum.value;
    // Setting Background color change handler
    red.oninput = () => {
        previewColor();
        updateLabel(redLab, red);
    };
    green.oninput = () => {
        previewColor();
        updateLabel(greenLab, green);
    };
    blue.oninput = () => {
        previewColor();
        updateLabel(blueLab, blue);
    };
    lum.oninput = () => {
        updateLabel(lumLab, lum);
    };
    // Buttons
    document.getElementById('on').onclick = () => display(fetch(new URL('/on', base)));
    document.getElementById('off').onclick = () => display(fetch(new URL('/off', base)));
    document.getElementById('rainbow').onclick = () => display(fetch(new URL('/rainbow', base)));
    console.log('set up!');
};

function updateLabel(label, slider) {
    label.innerHTML = slider.value;
}

function previewColor() {
    document.body.style.backgroundColor = `rgb(${red.value},${green.value},${blue.value})`;
}

function specialColor() {
    const url = new URL('/static', base);
    const params = {
        r: red.value,
        g: green.value,
        b: blue.value,
        l: lum.value
    };
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
    display(fetch(url));
}

async function display(reqToRes) {
    try {        
        const res = await reqToRes;
        if (res.ok) {
            output.innerHTML = res.text();    
        } else {
            output.innerHTML = `${res.status} -> ${res.statusText}`;
        }
    } catch (err) {
        output.innerHTML = 'bad error smh';
    }
}
