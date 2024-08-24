document
  .getElementById("predictionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById(
          "result"
        ).innerText = `Predicted House Price: $${data.prediction}`;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
