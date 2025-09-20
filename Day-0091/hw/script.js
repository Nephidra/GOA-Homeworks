const container = document.createElement("div");
container.style.width = "300px";
container.style.height = "500px";
container.style.border = "1px solid black";
container.style.overflow = "auto";
document.body.appendChild(container);

const colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "brown", "lime"];

for (let i = 0; i < 10; i++) {
    setTimeout(() => {
        const div = document.createElement("div");
        div.style.height = "50px";
        div.style.backgroundColor = colors[i];
        div.textContent = `Div ${i + 1}`;
        
        if (i % 2 === 0) {
            container.insertBefore(div, container.firstChild);
        } else {
            container.appendChild(div);
        }
    }, i * 500);
}