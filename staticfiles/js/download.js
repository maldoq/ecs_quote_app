// Fonction pour télécharger la carte
function downloadCard() {
    const card = document.getElementById('quoteCard');
    
    if (!card) {
        console.error('Quote card not found');
        return;
    }
    
    // Option 1: Utiliser html2canvas (si disponible)
    if (typeof html2canvas !== 'undefined') {
        downloadAsImage();
    } else {
        // Option 2: Télécharger comme HTML
        downloadAsHTML();
    }
}

// Télécharger comme image (nécessite html2canvas)
function downloadAsImage() {
    const card = document.getElementById('quoteCard');
    
    html2canvas(card, {
        backgroundColor: '#ffffff',
        scale: 2,
        logging: false,
    }).then(canvas => {
        const link = document.createElement('a');
        link.download = 'ma-citation-ecs-2026.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    });
}

// Télécharger comme HTML (méthode de secours)
function downloadAsHTML() {
    // Créer une nouvelle fenêtre avec la page de téléchargement
    const downloadUrl = window.location.origin + '/telecharger/' + userId + '/';
    window.open(downloadUrl, '_blank');
    
    // Alternative: télécharger directement
    setTimeout(() => {
        if (confirm('Voulez-vous télécharger votre carte?\n\nDans la nouvelle fenêtre, faites:\n- Ctrl+P (Windows/Linux) ou Cmd+P (Mac)\n- Puis "Enregistrer au format PDF"')) {
            // Rien à faire, l'utilisateur a déjà la fenêtre ouverte
        }
    }, 500);
}

// Ajouter une animation au survol du bouton de téléchargement
document.addEventListener('DOMContentLoaded', function() {
    const downloadBtn = document.querySelector('.download-button');
    
    if (downloadBtn) {
        downloadBtn.addEventListener('click', function() {
            // Animation du bouton
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    }
    
    // Animation d'apparition de la carte
    const card = document.getElementById('quoteCard');
    if (card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.8s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 300);
    }
});

// Fonction pour imprimer la carte
function printCard() {
    window.print();
}

// Ajouter des styles d'impression
const style = document.createElement('style');
style.textContent = `
    @media print {
        body * {
            visibility: hidden;
        }
        #quoteCard, #quoteCard * {
            visibility: visible;
        }
        #quoteCard {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
        }
        .action-buttons,
        .footer,
        .logo-container {
            display: none !important;
        }
    }
`;
document.head.appendChild(style);