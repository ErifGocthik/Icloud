(function select() {
   $(document).ready(function () {
      // let val = 'first';
      let sel = document.getElementById('select_id');
      // let opt = sel.options;
      let title_1 = document.getElementById('title_1');
      let list_cl = document.getElementsByClassName('click_me');
      // let val_list = [];
      let value_opt = null;
      let any_list = {1: '100', 2: '500',3: '1000', 4: '1500', 5: '2000', 6: '3000'};
      // val_list = sel.innerText.split('\n'); %=== Переносит все параметры в массив
      // console.log(sel.selectedIndex)
      $('#select_id').change(function (e) {
         value_opt = $('#select_id .click_me').innerHTML;
         console.log(value_opt);
         title_1.innerText = any_list[`${value_opt}`];
      });
   });
})();
//