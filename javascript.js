document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".nav-link");
    
    navLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Evita o comportamento padrão do link

            const sectionId = this.getAttribute("data-section");

            // Esconde todas as seções
            document.querySelectorAll(".content-section").forEach(section => {
                section.classList.remove("active");
            });

            // Mostra a seção correspondente
            document.getElementById(sectionId).classList.add("active");
        });
    });
});


let cameraStream = null;

document.addEventListener("DOMContentLoaded", function() {
  const navLinks = document.querySelectorAll(".nav-link");
  
  navLinks.forEach(link => {
    link.addEventListener("click", function(event) {
      event.preventDefault(); // Previne o comportamento padrão do link
      
      const sectionId = this.getAttribute("data-section");
      showSection(sectionId);
    });
  });
});

function showSection(sectionId) {
  // Esconde todas as seções
  document.querySelectorAll(".content-section").forEach(section => {
    section.classList.remove("active");
  });

  // Mostra a seção selecionada
  document.getElementById(sectionId).classList.add("active");

  // Se a seção for "camera", inicia a câmera; caso contrário, para a câmera se estiver ativa.
  if (sectionId === "camera") {
    startCamera();
  } else {
    stopCamera();
  }
}

function startCamera() {
  // Se já estiver ativo, não faz nada
  if (cameraStream) return;
  
  const videoElement = document.getElementById("cameraVideo");
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        cameraStream = stream;
        videoElement.srcObject = stream;
        // Tenta iniciar a reprodução explicitamente
        videoElement.play().catch(err => {
          console.error("Erro ao iniciar a reprodução do vídeo:", err);
        });
      })
      .catch(error => {
        console.error("Erro ao acessar a câmera:", error);
        // Exibe uma mensagem de erro caso não seja possível acessar a câmera
        videoElement.parentElement.innerHTML = "<p>Não foi possível acessar a câmera. Verifique as permissões e se o site está sendo servido via HTTPS.</p>";
      });
  } else {
    console.error("getUserMedia não suportado neste navegador.");
  }
}

function stopCamera() {
  if (cameraStream) {
    // Para todas as tracks do stream
    cameraStream.getTracks().forEach(track => track.stop());
    cameraStream = null;
    
    // Limpa o elemento de vídeo
    const videoElement = document.getElementById("cameraVideo");
    videoElement.srcObject = null;
  }
}
