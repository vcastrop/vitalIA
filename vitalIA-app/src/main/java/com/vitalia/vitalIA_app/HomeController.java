package com.vitalia_app;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String index() {
        return "index"; // This corresponds to "index.html"
    }

    @GetMapping("/appointment-rating-and-reviews")
    public String appointmentRatingAndReviews() {
        System.out.println("Appointment Rating and Reviews page accessed");
        return "appointment-rating-and-reviews";
    }

    @GetMapping("/schedule-medical-appointment")
    public String scheduleMedicalAppointment() {
        System.out.println("Schedule Medical Appointment page accessed");
        return "schedule-medical-appointment";
    }




    // Add more methods for other user stories as needed
}
