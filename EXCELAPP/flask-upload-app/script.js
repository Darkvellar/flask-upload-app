async function uploadFile(event) {
    event.preventDefault(); // Impede o recarregamento da página
  
    let fileInput = document.getElementById("file-upload");
    let responseMessage = document.getElementById("response-message");

    if (fileInput.files.length === 0) {
        alert("Por favor, selecione um arquivo!");
        return;
    }
  
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);
  
    try {
        let response = await fetch("https://cuddly-space-memory-694p7x9wx949f4x49-5501.app.github.dev/upload", {
            method: "POST",
            body: formData
        });
  
        let result = await response.json();
        responseMessage.innerText = result.message || result.error;
        responseMessage.style.opacity = "1"; // Exibe a mensagem

        // Esconde a mensagem após 7 segundos
        setTimeout(() => {
            responseMessage.style.opacity = "0";
        }, 7000);

    } catch (error) {
        responseMessage.innerText = "Erro ao enviar o arquivo.";
        responseMessage.style.opacity = "1";

        setTimeout(() => {
            responseMessage.style.opacity = "0";
        }, 7000);
    }
}
  
document.getElementById("upload-form").addEventListener("submit", uploadFile);


  