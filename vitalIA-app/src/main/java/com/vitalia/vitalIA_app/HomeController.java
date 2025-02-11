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

        return "medical-history-access"; // This corresponds to "medical-history-access.html"
    }

    @GetMapping("/medication-reminder")
    public String medicationReminder() {

        return "medication-reminder"; // This corresponds to "medication-reminder.html"
    }



    // Add more methods for other user stories as needed
}
