-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema parque_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema parque_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `parque_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci ;
USE `parque_db` ;

-- -----------------------------------------------------
-- Table `parque_db`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parque_db`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parque_db`.`visitas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parque_db`.`visitas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `parque` VARCHAR(45) NOT NULL,
  `fecha_visita` DATE NOT NULL,
  `rating` INT NOT NULL,
  `detalles` VARCHAR(255) NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_visitas_usuarios1_idx` (`usuarios_id`),
  CONSTRAINT `fk_visitas_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `parque_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parque_db`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parque_db`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuarios_id` INT NOT NULL,
  `visitas_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_usuarios_idx` (`usuarios_id`),
  INDEX `fk_likes_visitas1_idx` (`visitas_id`),
  CONSTRAINT `fk_likes_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `parque_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_visitas1`
    FOREIGN KEY (`visitas_id`)
    REFERENCES `parque_db`.`visitas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
