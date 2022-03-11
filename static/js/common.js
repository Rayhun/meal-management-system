$(".todoCheck2").click(function() {
    var id = $(this).val();

    $.ajax({
        url: "{% url 'package_info' %}",
        type: "GET",
        data: {
            'id': id,
        },
        success: function (data) {
            if (data.status == 'success') {
                location.reload();
            }
        }
    });
}
);