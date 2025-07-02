# equipo-naranjillo
# 📚 Práctica de Base de Datos SQL para Versionamiento de Código

## 📝 Descripción

En esta práctica se diseña y crea una base de datos SQL para gestionar usuarios, proyectos y commits en un sistema de control de versiones. El objetivo es comprender la estructura de datos relacional y aplicar conceptos de llaves primarias, foráneas e inserción de datos.

---

## 📂 Estructura de la Base de Datos

### Tablas

- **Usuarios**  
  Contiene información básica de los usuarios que participan en los proyectos.  
  - `id_usuario` (INT, PK, AUTO_INCREMENT)  
  - `nombre` (VARCHAR(50))  
  - `email` (VARCHAR(100), UNIQUE)  
  - `fecha_registro` (DATETIME, DEFAULT CURRENT_TIMESTAMP)

- **Proyectos**  
  Información de los proyectos gestionados por los usuarios.  
  - `id_proyecto` (INT, PK, AUTO_INCREMENT)  
  - `nombre` (VARCHAR(100))  
  - `descripcion` (TEXT)  
  - `fecha_creacion` (DATETIME, DEFAULT CURRENT_TIMESTAMP)  
  - `id_usuario` (INT, FK a Usuarios.id_usuario)

- **Commits**  
  Registro de commits realizados en los proyectos.  
  - `id_commit` (INT, PK, AUTO_INCREMENT)  
  - `mensaje` (VARCHAR(255))  
  - `fecha_commit` (DATETIME, DEFAULT CURRENT_TIMESTAMP)  
  - `id_proyecto` (INT, FK a Proyectos.id_proyecto)  
  - `id_usuario` (INT, FK a Usuarios.id_usuario)

---

## 🔧 Script SQL Utilizado

```sql
-- Crear la base de datos
CREATE DATABASE PracticaVersionamiento;
USE PracticaVersionamiento;

-- Crear tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla Proyectos
CREATE TABLE Proyectos (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Commits
CREATE TABLE Commits (
    id_commit INT AUTO_INCREMENT PRIMARY KEY,
    mensaje VARCHAR(255) NOT NULL,
    fecha_commit DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_proyecto INT,
    id_usuario INT,
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Insertar datos en Usuarios
INSERT INTO Usuarios (nombre, email) VALUES
('Ana Perez', 'ana.perez@example.com'),
('Luis Garcia', 'luis.garcia@example.com'),
('Maria Rodriguez', 'maria.rodriguez@example.com');

-- Insertar datos en Proyectos
INSERT INTO Proyectos (nombre, descripcion, id_usuario) VALUES
('Proyecto Control de Versiones', 'Sistema para practicar versionamiento con Git', 1),
('App Móvil de Tareas', 'Aplicación para gestionar tareas diarias', 2);

-- Insertar datos en Commits
INSERT INTO Commits (mensaje, id_proyecto, id_usuario) VALUES
