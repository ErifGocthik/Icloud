(function modal() {
    $(document).ready(function() {
        let modal_win = document.getElementById('modal_WIN_FORM');
        $('.create_new_archive_btn').mousedown(function (e) {
           $(modal_win).css({'visibility': 'visible', 'z-index': '50'});
            $('.create_new_archive_btn').mouseup(function (e) {
           $(modal_win).css({'visibility': 'hidden', 'z-index': '-50'});
        });
        });
    });
})();