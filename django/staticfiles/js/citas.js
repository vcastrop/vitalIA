$(document).ready(function () {
    // Cargar doctores según especialidad seleccionada
    $("#especialidad").change(function () {
        let especialidadId = $(this).val();
        let doctorSelect = $("#doctor");

        doctorSelect.html("<option value=''>Cargando...</option>");

        if (especialidadId) {
            $.get(obtenerDoctoresUrl + "?especialidad_id=" + especialidadId, function (data) {
                doctorSelect.html("<option value=''>Seleccione un doctor</option>");
                data.doctores.forEach(function (doctor) {
                    doctorSelect.append(`<option value="${doctor.id}">${doctor.nombre}</option>`);
                });
            }).fail(function () {
                doctorSelect.html("<option value=''>Error al cargar doctores</option>");
            });
        } else {
            doctorSelect.html("<option value=''>Seleccione una especialidad primero</option>");
        }
    });

    // Buscar citas médicas disponibles
    $("#form-busqueda").submit(function (event) {
        event.preventDefault();
        let fecha = $("#fecha").val();
        let especialidad = $("#especialidad").val();
        let doctor = $("#doctor").val();

        if (fecha && especialidad && doctor) {
            $.get(buscarCitasUrl + "?fecha=" + fecha + "&especialidad=" + especialidad + "&doctor=" + doctor, function (data) {
                let tabla = $("#tabla-citas");
                tabla.empty();

                if (data.citas.length > 0) {
                    data.citas.forEach(function (cita) {
                        tabla.append(
                            `<tr>
                                <td>${cita.fecha}</td>
                                <td>${cita.hora}</td>
                                <td>
                                    <button class="agendar-btn" data-id="${cita.id}">Agendar</button>
                                </td>
                            </tr>`
                        );
                    });

                    // Evento de agendar cita
                    $(".agendar-btn").on("click", function () {
                        let citaId = $(this).data("id");

                        $.ajax({
                            url: reservarCitaUrl,
                            type: "POST",
                            contentType: "application/json",
                            data: JSON.stringify({ cita_id: citaId }),
                            headers: { "X-CSRFToken": csrfToken }, // Agregar token CSRF
                            success: function (response) {
                                alert(response.mensaje);
                                location.reload();
                            },
                            error: function (xhr) {
                                alert("Error al agendar la cita: " + xhr.responseText);
                            }
                        });
                    });

                } else {
                    tabla.append("<tr><td colspan='3'>No hay citas disponibles</td></tr>");
                }
            });
        } else {
            alert("Por favor, seleccione fecha, especialidad y doctor.");
        }
    });
});