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

    // Add more methods for other user stories as needed
}
