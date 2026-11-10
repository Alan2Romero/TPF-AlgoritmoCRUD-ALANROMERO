-- TABLAS --
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);

-- INSERCION DE DATOS DE PRUEBA --
INSERT INTO categorias (nombre) VALUES ('Electrónica');
INSERT INTO categorias (nombre) VALUES ('Hogar');

INSERT INTO productos (nombre, precio, categoria_id) VALUES ('Auriculares Bluetooth', 45.99, 1);
INSERT INTO productos (nombre, precio, categoria_id) VALUES ('Lámpara LED', 15.50, 2);