package com.example.a7last.model.type;

import com.example.a7last.model.value.StringValue;
import com.example.a7last.model.value.Value;

public class StringType implements Type{
    @Override
    public boolean equals(Type anotherType) {
        return anotherType instanceof StringType;
    }

    @Override
    public Value defaultValue() {
        return new StringValue("");
    }

    @Override
    public Type deepCopy() {
        return new StringType();
    }

    @Override
    public String toString() {
        return "string";
    }
}
