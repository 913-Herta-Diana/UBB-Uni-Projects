package com.example.a7last.model.type;

import com.example.a7last.model.value.Value;

public interface Type {
    boolean equals(Type anotherType);
    Value defaultValue();
    Type deepCopy();
}
