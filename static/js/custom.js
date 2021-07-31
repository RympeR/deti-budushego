function add_coupon() {
    $.ajax({
        url: '{% url "shop_section:add_coupon" %}',
        type: "post",
        data: {
            coupon: $("#coupon").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },

        success: function (result) {
            location.reload();
        },
        error: function (result) {
            console.log(result, "location is bad");
        },
    });
}
function send_order_data() {
        $(document).ready(()=>{$('#subm').click();});
}