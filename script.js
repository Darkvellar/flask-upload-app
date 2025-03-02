document.getElementById("upload-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Impede o recarregamento da página
  
    let fileInput = document.getElementById("file-upload");
    if (fileInput.files.length === 0) {
      alert("Por favor, selecione um arquivo!");
      return;
    }
  
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);
  
    try {
      // Usamos URL relativa para funcionar tanto no Codespaces quanto localmente
      let response = await fetch("/upload", {
        method: "POST",
        body: formData
      });
  
      let result = await response.json();
      document.getElementById("response-message").innerText = result.message || result.error;
    } catch (error) {
      document.getElementById("response-message").innerText = "Erro ao enviar o arquivo.";
    }
  });
  
