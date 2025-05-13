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

/* Show Gallery  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
    const galleryButton = document.getElementById('showGalleryButton');
    if (galleryButton) {
        galleryButton.addEventListener('click', toggleGallerySection);
    }
});

/* Show Custom Type  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const typeField = document.querySelector('#id_type');
  const customTypeWrapper = document.querySelector('#custom-type-wrapper');

  if (!typeField || !customTypeWrapper) return;

  function toggleCustomType() {
    if (typeField.value === 'other') {
      customTypeWrapper.style.display = 'block';
    } else {
      customTypeWrapper.style.display = 'none';
    }
  }

  toggleCustomType();
  typeField.addEventListener('change', toggleCustomType);
});

/* Show Delete Offer Modal  ----------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
  const deleteModal = document.getElementById('globalDeleteOfferModal');
  deleteModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const offerId = button.getAttribute('data-offer-id');
    const propertyName = button.getAttribute('data-property-name');
    const urlTemplate = button.getAttribute('data-url-template');

    // Update property name in the modal
    document.getElementById('propertyNamePlaceholder').textContent = propertyName;

    // Replace 0 in template with actual offerId
    const actionUrl = urlTemplate.replace('0', offerId);

    // Set form action
    document.getElementById('deleteOfferForm').action = actionUrl;
  });
});

/* Show Delete Property Modal and Gallery Navigation ---------------------------------------------- */
document.addEventListener('DOMContentLoaded', function () {
    // Get photos from JSON script
    const photos = JSON.parse(document.getElementById('gallery-photos').textContent);
    let currentImageIndex = 0;

    // Select elements
    const mainImage = document.getElementById('mainImage');
    const prevBtn = document.getElementById('prevMainImageBtn');
    const nextBtn = document.getElementById('nextMainImageBtn');

    // Function to update main image
    const updateMainImage = () => {
        if (photos.length > 0) {
            mainImage.src = photos[currentImageIndex].image;
        }
    };

    // Next image
    nextBtn.addEventListener('click', function () {
        currentImageIndex = (currentImageIndex + 1) % photos.length;
        updateMainImage();
    });

    // Previous image
    prevBtn.addEventListener('click', function () {
        currentImageIndex = (currentImageIndex - 1 + photos.length) % photos.length;
        updateMainImage();
    });

    // Optional: Update main image if someone clicks a sidebar thumbnail
    document.querySelectorAll('.property-sidebar-thumb img').forEach((thumb, index) => {
        thumb.addEventListener('click', function () {
            currentImageIndex = (index + 1) % photos.length;  // +1 because first is already shown
            updateMainImage();
        });
    });
});



