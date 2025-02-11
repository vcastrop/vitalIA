package com.vitalia_app;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String index() {
        return "index"; // Main page
    }

    @GetMapping("/menstrual-cycle-tracker")
    public String menstrual-cycle-tracker() {
        return "menstrual-cycle-tracker"; // Menstrual cycle tracker page
    }
}
