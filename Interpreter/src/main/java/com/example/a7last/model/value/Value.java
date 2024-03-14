package com.example.a7last.model.value;

import com.example.a7last.model.type.Type;

public interface Value {
    Type getType();
    Value deepCopy();
}
