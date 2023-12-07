<script>

    function p_button() {

        $('#button').css('background-color', 'grey');
    $('#button').css('color', 'black');

    }

    function dp_button() {

        $('#button').css('background-color', 'black');
    $('#button').css('color', 'white');

    }

    $('#button').mouseover(p_button);
    $('#button').mouseout(dp_button);

    function textarea_1() {

        $('#id_name').css('background-color', '#adabaf');

    }
    $('#id_name').focus(textarea_1);

</script>