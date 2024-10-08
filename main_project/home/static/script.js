
document.addEventListener("DOMContentLoaded", function(){
    document.querySelectorAll('.sidebar .nav-link').forEach(function(element){

        // Show submenu on hover
        element.addEventListener('mouseover', function (e) {

            let nextEl = element.nextElementSibling;
            let parentEl  = element.parentElement;

            if(nextEl) {
                e.preventDefault();
                let mycollapse = new bootstrap.Collapse(nextEl, {
                    toggle: false // Don't immediately toggle, just control via show/hide
                });

                if (!nextEl.classList.contains('show')) {
                    mycollapse.show();
                }

                // Close other open submenus
                var opened_submenu = parentEl.parentElement.querySelector('.submenu.show');
                if(opened_submenu && opened_submenu !== nextEl) {
                    new bootstrap.Collapse(opened_submenu, {
                        toggle: false
                    }).hide();
                }
            }
        });

        // Hide submenu when mouse leaves
        element.addEventListener('mouseout', function (e) {
            let nextEl = element.nextElementSibling;

            if(nextEl && nextEl.classList.contains('show')) {
                let mycollapse = new bootstrap.Collapse(nextEl, {
                    toggle: false
                });
                mycollapse.hide();
            }
        });
    });
});