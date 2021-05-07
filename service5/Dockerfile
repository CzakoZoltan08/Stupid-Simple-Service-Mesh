#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:3.1 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /src
COPY ["service5.csproj", "."]
RUN dotnet restore "./service5.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "service5.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "service5.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "service5.dll"]