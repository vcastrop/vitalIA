package com.vitalia_app;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String index() {
        return "index"; // This corresponds to "index.html"
    }
    @GetMapping("/Formula-and-Medications-Management")
    public String FormulaandMedicationsManagement() {
        System.out.println("Formula and Medications Management");
        return "Formula-and-Medications-Management";
    }
}

}
