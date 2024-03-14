module com.example.a7last {
    requires javafx.controls;
    requires javafx.fxml;

    //requires org.controlsfx.controls;

    opens com.example.a7last to javafx.fxml;
    exports com.example.a7last;

    exports com.example.a7last.controller;
    opens com.example.a7last.controller to javafx.fxml;
    //exports com.example.a7last.gui to javafx.graphics;
    exports com.example.a7last.gui to javafx.fxml;
    opens com.example.a7last.gui to javafx.fxml;
    //exports com.example.a7last to javafx.graphics;

}