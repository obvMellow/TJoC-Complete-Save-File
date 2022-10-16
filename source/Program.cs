using System;
using System.IO;

namespace Installer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This proccess will delete your current progress!");
            start:
                Console.Write("Do you want to continue? (y/n): ");
                string answer = Console.ReadLine();

                switch (answer)
                {
                    case "y": goto installer;

                    case "n": Environment.Exit(0); break;

                    default: goto start;
                }
            
            installer:
                Installer();
        }
        static void Installer()
        {
            string username = Environment.UserName;
            string currentDir = Directory.GetCurrentDirectory();
            string sourceDir = $"{currentDir}\\SaveGames";
            string destDir = $"C:\\Users\\{username}\\Appdata\\Local\\TJoC_SM\\Saved\\SaveGames\\";
            string[] sourceFiles = Directory.GetFiles(sourceDir);
            string destFile;

            Console.WriteLine("\nCopying the files...\n");
            Thread.Sleep(100);
            for (int i = 0; i < sourceFiles.Length; i++)
            {
                destFile = sourceFiles[i].Substring(sourceDir.Length + 1);
                File.Copy(sourceFiles[i], destDir + destFile, true);
                Console.WriteLine($"Copied {destFile}.");

            }
            Console.WriteLine("\nAll files were copied successfully!");
            Console.WriteLine("\nPress any key to exit.");
            Console.ReadKey();
        }
    }
}