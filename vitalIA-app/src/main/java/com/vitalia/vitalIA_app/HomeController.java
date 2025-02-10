package com.vitalia_app;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String index() {
        return "index"; // This corresponds to "index.html"
    }

    @GetMapping("/medical-history-access")
    public String medicalHistoryAccess() {
        System.out.println("Medical History Access page accessed");
        return "medical-history-access"; // This corresponds to "medical-history-access.html"
    }

    @GetMapping("/medication-reminder")
    public String medicationReminderAccess() {
        System.out.println("Medical Reminder Access page accessed");
        return "medication-reminder"; // This corresponds to "medical-history-access.html"
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

    @GetMapping("/formula-and-medications-management")
    public String formulaAndMedicationsManagement() {
        System.out.println("Formula and Medications Management page accessed");
        return "formula-and-medications-management";
    }


    // Add more methods for other user stories as needed
}
