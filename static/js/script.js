const form = document.querySelector(".form");
const output = document.createElement("p"); // Create a new paragraph element for the estimated price

form.addEventListener("submit", function(event){
    event.preventDefault();
    validateForm();
});

function validateForm() {
    const carat = document.getElementById("carat").value.trim();
    const depth = document.getElementById("depth").value.trim();
    const table = document.getElementById("table").value.trim();
    const x = document.getElementById("x").value.trim();
    const y = document.getElementById("y").value.trim();
    const z = document.getElementById("z").value.trim();
    const cut = document.getElementById("cut").value.trim();
    const color = document.getElementById("color").value.trim();
    const clarity = document.getElementById("clarity").value.trim();


    const regex = /^\d+(\.\d+)?$/;

    if (![carat, depth, table, x, y, z].every(test => test !== "" && regex.test(test))) {
        output.innerText = "";
        output.classList.remove("visible");
        document.getElementById("error-create").classList.remove("hidden");
    } else {
        document.getElementById("error-create").classList.add("hidden");
        sendDataToServer(carat, depth, table, x, y, z, cut, color, clarity);
    }
}

function sendDataToServer(carat, depth, table, x, y, z, cut, color, clarity) {
    const formData = new FormData();
    formData.append("carat", carat);
    formData.append("depth", depth);
    formData.append("table", table);
    formData.append("x", x);
    formData.append("y", y);
    formData.append("z", z);
    formData.append("cut", cut);
    formData.append("color", color);
    formData.append("clarity", clarity);

    fetch("/", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Handle the server response
        const estimatedPrice = parseFloat(data).toLocaleString(); // Convert the response to a float and add comma separator
        output.innerText = "Estimated Price: $" + estimatedPrice;
        document.getElementById("output").appendChild(output); // Append the paragraph element to the output div
    })
    .catch(error => {
        // Handle any errors
        console.error(error);
    });
}

function closeError() {
    document.getElementById("error-create").classList.add("hidden");
}
