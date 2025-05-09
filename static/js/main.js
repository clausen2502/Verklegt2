/* Location Filter JavaScript ---------------------------------------------------------------------- */
function toggleLocationDropdown() {
    toggleDropdown('locationDropdown');
}

/* Type Filter JavaScript -------------------------------------------------------------------------- */
function toggleTypeDropdown() {
    toggleDropdown('typeDropdown');
}

/* Size Filter JavaScript -------------------------------------------------------------------------- */
function toggleSizeDropdown() {
    toggleDropdown('sizeDropdown');
}

/* Room Filter JavaScript -------------------------------------------------------------------------- */
function toggleRoomDropdown() {
    toggleDropdown('roomDropdown');
}
/* Price Filter JavaScript -------------------------------------------------------------------------- */
function togglePriceDropdown() {
    toggleDropdown('priceDropdown');
}

/* General Dropdown Toggle Function ---------------------------------------------------------------- */
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
}

/* Gallery Toggle JavaScript ----------------------------------------------------------------------- */
function toggleGallerySection() {
    const section = document.getElementById('extra-gallery');
    const galleryButtonText = document.querySelector('#showGalleryButton p');

    if (!section || !galleryButtonText) return;

    if (section.style.display === 'none' || section.style.display === '') {
        section.style.display = 'flex';
        galleryButtonText.textContent = 'Hide Gallery';
    } else {
        section.style.display = 'none';
        galleryButtonText.textContent = '30 MYNDIR';
    }
}

/* DOMContent Loaded Handler ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
    const galleryButton = document.getElementById('showGalleryButton');
    if (galleryButton) {
        galleryButton.addEventListener('click', toggleGallerySection);
    }
});


