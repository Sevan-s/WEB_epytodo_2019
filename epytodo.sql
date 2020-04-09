
CREATE Database epytodo;
use epytodo;

CREATE TABLE IF NOT EXISTS `task` (
  `task_id` int NOT NULL AUTO_INCREMENT,
  `title` char(20) NOT NULL,
  `begin` date NOT NULL DEFAULT CURDATE(),
  `end` date NULL,
  `status` enum('not started','in progress','done') NOT NULL DEFAULT 'not started',
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `task` WRITE;

UNLOCK TABLES;

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` char(20) NOT NULL,
  `password` char(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `user` WRITE;

UNLOCK TABLES;


CREATE TABLE IF NOT EXISTS `user_has_task` (
  `fk_user_id` int NOT NULL,
  `fk_task_id` int NOT NULL,
  KEY `fk_user_id` (`fk_user_id`),
  KEY `fk_task_id` (`fk_task_id`),
  CONSTRAINT `user_has_task_ibfk_1` FOREIGN KEY (`fk_user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `user_has_task_ibfk_2` FOREIGN KEY (`fk_task_id`) REFERENCES `task` (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `user_has_task` WRITE;


UNLOCK TABLES;
