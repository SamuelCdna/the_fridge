-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema my_fridge
-- -----------------------------------------------------
-- 
-- 

-- -----------------------------------------------------
-- Schema my_fridge
--
-- 
-- 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_fridge` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema gamesshop
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gamesshop
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gamesshop` DEFAULT CHARACTER SET utf8mb3 ;
USE `my_fridge` ;

-- -----------------------------------------------------
-- Table `my_fridge`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`users` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(250) NULL,
  `level` INT NULL,
  `permisions` VARCHAR(50) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`categorys`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`categorys` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`categorys` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`recipes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`recipes` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NULL,
  `time_cook` INT NULL,
  `level_recipe` VARCHAR(45) NULL,
  `preference` INT NULL,
  `food_type` INT NULL,
  `recipescol` VARCHAR(45) NULL,
  `description` TEXT(1000) NULL,
  `preparation` TEXT(3000) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_recipes_categorys1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `my_fridge`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipes_categorys1`
    FOREIGN KEY (`category_id`)
    REFERENCES `my_fridge`.`categorys` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`ingredients`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`ingredients` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`ingredients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `amount` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`ingrediente_receta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`ingrediente_receta` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`ingrediente_receta` (
  `ingredient_id` INT NOT NULL,
  `recipe_id` INT NOT NULL,
  PRIMARY KEY (`ingredient_id`, `recipe_id`),
  INDEX `fk_ingredients_has_recipes_recipes1_idx` (`recipe_id` ASC) VISIBLE,
  INDEX `fk_ingredients_has_recipes_ingredients1_idx` (`ingredient_id` ASC) VISIBLE,
  CONSTRAINT `fk_ingredients_has_recipes_ingredients1`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `my_fridge`.`ingredients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingredients_has_recipes_recipes1`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `my_fridge`.`recipes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `gamesshop` ;

-- -----------------------------------------------------
-- Table `gamesshop`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gamesshop`.`users` ;

CREATE TABLE IF NOT EXISTS `gamesshop`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(155) NULL DEFAULT NULL,
  `last_name` VARCHAR(155) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `rol` TINYINT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_estonian_ci
COMMENT = '					';


-- -----------------------------------------------------
-- Table `gamesshop`.`juegos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gamesshop`.`juegos` ;

CREATE TABLE IF NOT EXISTS `gamesshop`.`juegos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(155) NULL DEFAULT NULL,
  `categoria` TINYINT NULL DEFAULT NULL,
  `precio` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_juegos_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_juegos_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `gamesshop`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gamesshop`.`compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gamesshop`.`compras` ;

CREATE TABLE IF NOT EXISTS `gamesshop`.`compras` (
  `juego_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `adress` VARCHAR(255) NULL DEFAULT NULL,
  `costo` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`juego_id`, `user_id`),
  INDEX `fk_juegos_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_juegos_has_users_juegos1_idx` (`juego_id` ASC) VISIBLE,
  CONSTRAINT `fk_juegos_has_users_juegos1`
    FOREIGN KEY (`juego_id`)
    REFERENCES `gamesshop`.`juegos` (`id`),
  CONSTRAINT `fk_juegos_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `gamesshop`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gamesshop`.`favoritos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gamesshop`.`favoritos` ;

CREATE TABLE IF NOT EXISTS `gamesshop`.`favoritos` (
  `user_id` INT NOT NULL,
  `juego_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `juego_id`),
  INDEX `fk_users_has_juegos_juegos1_idx` (`juego_id` ASC) VISIBLE,
  INDEX `fk_users_has_juegos_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_juegos_juegos1`
    FOREIGN KEY (`juego_id`)
    REFERENCES `gamesshop`.`juegos` (`id`),
  CONSTRAINT `fk_users_has_juegos_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `gamesshop`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_estonian_ci;


-- -----------------------------------------------------
-- Table `gamesshop`.`reseñas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gamesshop`.`reseñas` ;

CREATE TABLE IF NOT EXISTS `gamesshop`.`reseñas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL DEFAULT NULL,
  `rate` TINYINT NULL DEFAULT NULL,
  `Juego` TINYINT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ideas_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_ideas_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `gamesshop`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 41
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_estonian_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
